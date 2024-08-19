let videoQueue = [];
let currentVideoIndex = 0;

function getYouTubeVideoId(url) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
}

function addVideoToQueue() {
    const url = document.getElementById('youtubeUrl').value;
    const videoId = getYouTubeVideoId(url);
    if (videoId) {
        videoQueue.push(videoId);
        displayQueue();
        document.getElementById('youtubeUrl').value = ''; // Clear input field
    } else {
        alert('Invalid YouTube URL');
    }
}

function displayQueue() {
    const queueDiv = document.getElementById('videoQueue');
    queueDiv.innerHTML = ''; // Clear previous queue
    videoQueue.forEach((videoId, index) => {
        const videoItem = document.createElement('div');
        videoItem.textContent = `Video ${index + 1}: https://www.youtube.com/watch?v=${videoId}`;
        queueDiv.appendChild(videoItem);
    });
}

function loadNextVideo() {
    if (currentVideoIndex < videoQueue.length) {
        const videoId = videoQueue[currentVideoIndex];
        const iframe = document.createElement('iframe');
        iframe.width = '560';
        iframe.height = '315';
        iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
        iframe.frameBorder = '0';
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
        iframe.allowFullscreen = true;

        const playerDiv = document.getElementById('youtubePlayer');
        playerDiv.innerHTML = ''; // Clear previous video
        playerDiv.appendChild(iframe);

        currentVideoIndex++;
    } else {
        alert('No more videos in the queue');
    }
}

document.getElementById('youtubeUrl').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        addVideoToQueue();
    }
});
