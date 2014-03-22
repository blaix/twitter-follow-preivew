$(".tweet").each(function(i) {
    $tweet = $(this);
    if($tweet.data("is-reply-to")) {
        alert($tweet.find(".tweet-text").text());
    }
});
