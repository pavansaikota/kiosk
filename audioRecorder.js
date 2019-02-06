let mediaRecorder;
const audioChunks = [];

const start = () => {
    mediaRecorder.start();
};

const recordAudio = () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.addEventListener("dataavailable", event => {
          audioChunks.push(event.data);
        });

    });       
};

const stop = () => {
    mediaRecorder.addEventListener("stop", () => {
      const audioBlob = new Blob(audioChunks);
      const audioUrl = URL.createObjectURL(audioBlob);
      const audio = new Audio(audioUrl);
      const play = () => {
        audio.play();
      };
    });

    mediaRecorder.stop();
};

recordAudio();