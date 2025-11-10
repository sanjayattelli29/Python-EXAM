// Block any attempt to go fullscreen
document.addEventListener("fullscreenchange", () => {
    if (document.fullscreenElement) {
        document.exitFullscreen();
        console.log("Blocked fullscreen attempt!");
    }
});

// Also override the API directly
Element.prototype.requestFullscreen = function() {
    console.log("Blocked requestFullscreen()");
};
