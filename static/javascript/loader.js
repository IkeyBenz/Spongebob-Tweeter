$(document).ready(function () {
    $('#newTweetBtn').click(getNewTweet);
});

function getNewTweet() {
    fetch('/tweets').then(res => {
        return res.json();
    }).then(json => {
        $('#output').text(json.tweet);
    });
}