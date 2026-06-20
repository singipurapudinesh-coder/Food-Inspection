function startVoice() {

    if (!('webkitSpeechRecognition' in window)) {

        alert(
            "Voice recognition works only in Google Chrome."
        );

        return;
    }

    const recognition =
        new webkitSpeechRecognition();

    recognition.lang = "en-US";

    recognition.continuous = false;

    recognition.interimResults = false;

    recognition.start();

    recognition.onresult = function (event) {

        const text =
            event.results[0][0].transcript;

        document.getElementById(
            "prompt"
        ).value = text;
    };

    recognition.onerror = function (event) {

        console.log(event.error);

        alert(
            "Voice recognition failed."
        );
    };

    recognition.onend = function () {

        console.log(
            "Voice recognition stopped."
        );
    };
}