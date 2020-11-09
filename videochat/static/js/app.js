navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia
    || navigator.mozGetUserMedia || navigator.msGetUserMedia;
window.URL = window.URL || window.webkitURL;
const myVideo = document.createElement('video');
myVideo.muted = true;
const videoGrid = document.getElementById('video-grid');
const socket = io('//localhost:5000');
const peers = {};
const options = {
	optional: [
		{DtlsSrtpKeyAgreement: true}, // требуется для соединения между Chrome и Firefox
		{RtpDataChannels: true} // требуется в Firefox для использования DataChannels API
	]
};
const iceServers = {
    iceServers: [
        {url: 'stun:stun.l.google.com:19302'},
        {url: 'stun:stun1.l.google.com:19302'},
        {url: 'stun:stun2.l.google.com:19302'},
        {url: 'stun:stun3.l.google.com:19302'},
        {url: 'stun:stun4.l.google.com:19302'},
        {url: 'stun:stun.voipinfocenter.com:3478'},
        {url: 'stun:stun.voipplanet.nl:3478'},
        {url: 'stun:stun.voippro.com:3478'},
        {url: 'stun:stun.voipraider.com:3478'},
        {url: 'stun:stun.voipstunt.com:3478'},
        {url: 'stun:stun.voipwise.com:3478'},
        {url: 'stun:stun.voipzoom.com:3478'},
    ]
};
const pc = new RTCPeerConnection(iceServers, options);

socket.on('user-connected', function (userId) {

});

socket.on('user-disconnected', function (userId) {

});

pc.addEventListener('addstream', function(stream) {
    let video = document.createElement('video');
    createVideo(video, stream);
});

navigator.getUserMedia({video: true, audio: true},
    function (stream) {
        createVideo(myVideo, stream);
        console.log(stream);
        socket.emit('join-room', room_id, stream);
        socket.on('user-connected', function (userId) {

        });
    },
    function (error) {
        console.log(error);
    });

function createVideo(video, stream) {
    video.srcObject = stream;
    video.addEventListener('loadedmetadata', () => {
        video.play()
    });
  videoGrid.append(video)
}