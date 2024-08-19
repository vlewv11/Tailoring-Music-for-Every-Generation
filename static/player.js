initial_songs = [];
recommended_songs = [];
let currentSongIndex = 0;
let currentPlaylist = "initial-playlist";
const audioElement = document.getElementById("audio");

function filterArray(songs) {
    // return songs.filter((song) => song.track_name && song.track_demo);
    return songs.filter((song) => song.track_name);
}

document.addEventListener("DOMContentLoaded", async () => {
    const indexData = document.getElementById("flaskData").dataset.index;

    try {
        const initialResponse = await fetch(`/get-playlist?index=${indexData}&is_initial=false`);
        const initialSongs = await initialResponse.json();
        initial_songs = filterArray(initialSongs);
        populatePlaylist("initial-playlist");

        const recommendedResponse = await fetch(`/get-playlist?index=${indexData}&is_initial=true`);
        const recommendedSongs = await recommendedResponse.json();
        recommended_songs = filterArray(recommendedSongs);
        populatePlaylist("recommended-playlist");
    } catch (error) {
        console.error("Error fetching playlist:", error);
    }
});

function populatePlaylist(playlist_name) {
    var playlist = document.getElementById(playlist_name);
    playlist.innerHTML = ""; // Clear any existing content
    songs = playlist_name === "recommended-playlist" ? recommended_songs : initial_songs;
    songs.forEach((song, index) => {
        var li = document.createElement("li");
        li.textContent = song.track_name;
        li.dataset.index = index;
        li.onclick = () => highlightSong(playlist_name, index);
        playlist.appendChild(li);
    });
}

function highlightSong(playlist_name, songIndex) {
    // Remove the "highlighted" class from all <li> elements
    const playlistItems = document.querySelectorAll(`#${playlist_name} li`);
    playlistItems.forEach((item) => item.classList.remove("highlighted"));
    const anotherPlaylistItems = document.querySelectorAll(
        `#${playlist_name === "initial-playlist" ? "recommended-playlist" : "initial-playlist"} li`
    );
    anotherPlaylistItems.forEach((item) => item.classList.remove("highlighted"));
    const songToHighlight = playlistItems[songIndex];
    songToHighlight.classList.add("highlighted");

    const selectedSong =
        playlist_name === "recommended-playlist" ? recommended_songs[songIndex] : initial_songs[songIndex];
    currentSongIndex = songIndex;
    currentPlaylist = playlist_name;

    updatePlayer(selectedSong);
}

function updatePlayer(song) {
    const audioSource = document.getElementById("audioSource");
    const audioPlayerImage = document.getElementById("player-image");
    const songName = document.getElementById("song-name");

    audioSource.src = song.track_demo;
    track_cover = song.track_cover;
    audioPlayerImage.src = track_cover === null ? "https://iili.io/HlHy9Yx.png" : track_cover;
    songName.textContent = song.track_name;

    audioElement.load();
    audioElement.play();
    document.getElementById("playPauseIcon").classList.replace("fa-play", "fa-pause");
}

function togglePlayPause() {
    if (audioElement.paused) {
        audioElement.play();
        document.getElementById("playPauseIcon").classList.replace("fa-play", "fa-pause");
    } else {
        audioElement.pause();
        document.getElementById("playPauseIcon").classList.replace("fa-pause", "fa-play");
    }
}

function prevSong() {
    if (currentPlaylist === "recommended-playlist") {
        if (currentSongIndex > 0) {
            currentSongIndex--;
        } else {
            currentSongIndex = initial_songs.length - 1;
            currentPlaylist = "initial-playlist";
        }
    } else {
        if (currentSongIndex > 0) {
            currentSongIndex--;
        } else {
            currentSongIndex = recommended_songs.length - 1;
            currentPlaylist = "recommended-playlist";
        }
    }
    highlightSong(currentPlaylist, currentSongIndex);
}

function nextSong() {
    if (currentPlaylist === "recommended-playlist") {
        if (currentSongIndex < recommended_songs.length - 1) {
            currentSongIndex++;
        } else {
            currentSongIndex = 0;
            currentPlaylist = "initial-playlist";
        }
    } else {
        if (currentSongIndex < initial_songs.length - 1) {
            currentSongIndex++;
        } else {
            currentSongIndex = 0;
            currentPlaylist = "recommended-playlist";
        }
    }
    highlightSong(currentPlaylist, currentSongIndex);
}
