
var camera_button = document.querySelector("#start-camera");
var video = document.querySelector("#video");
var canvas = document.querySelector("#canvas");

camera_button.addEventListener('click', async function() {
    let stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    video.srcObject = stream;
    click()
});

function click(){
    addEventListener('keydown', (e)=> {
    if(e.key === ' '){
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    var image_data_url = canvas.toDataURL('image/jpeg');
    console.log(image_data_url);

    }
    
    })}

