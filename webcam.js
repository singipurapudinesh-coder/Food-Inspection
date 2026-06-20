async function startCamera() {

    try {

        const stream = await navigator.mediaDevices.getUserMedia({

            video: true,

            audio: false

        });

        const video = document.getElementById(

            "camera"

        );

        video.srcObject = stream;

    }

    catch (error) {

        console.log(error);

        alert(

            "Please allow camera permission."

        );
    }
}