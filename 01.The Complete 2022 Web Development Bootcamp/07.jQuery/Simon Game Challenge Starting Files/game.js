const buttonColours = ["red", "blue", "green", "yellow"];
let gamePattern = [];
let userClickedPattern = [];
let started = false;
let level = 0;

$(".btn").click(function() {
    let userChosenColour = $(this).attr("id");
    userClickedPattern.push(userChosenColour);
    playSound(userChosenColour);
    animatePress(userChosenColour);
    if (userClickedPattern.length == level) {
        checkAnswer(level - 1);
        setTimeout(() => {
            nextSequence()
        }, 1000);
    }
});

$(document).keypress(() => {
    if (!started) {
        $("#level-title").text("Level " + level);
        started = true;
        nextSequence();
    }
})

function nextSequence() {
    if (started) {
        level++;
        $("#level-title").text("Level " + level);
        let randomNumber = Math.floor(Math.random() * 4);
        let randomChosenColour = buttonColours[randomNumber];
        gamePattern.push(randomChosenColour);
        $("#" + randomChosenColour).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
        playSound(randomChosenColour);
        userClickedPattern = [];
    }
}

function playSound(name) {
    let audio = new Audio("./sounds/" + name + ".mp3");
    audio.play();
}

function animatePress(currentColour) {
    $("#" + currentColour).addClass("pressed");
    setTimeout(() => {
        $("#" + currentColour).removeClass("pressed")
    }, 100);
}

function checkAnswer(currentLevel) {
    if (gamePattern[currentLevel] == userClickedPattern[currentLevel]) {
        
    } else {
        $("body").addClass("game-over");
        setTimeout(() => {
            $("body").removeClass("game-over");
        }, 200);
        $("h1").text("Game Over, Press Any Key to Restart");
        playSound("wrong");
        startOver();
    }
}

function startOver() {
    level = 0;
    gamePattern = [];
    userClickedPattern = [];
    started = false;
}