$(document).ready(function () {
    var $player = $('#player');
    var $nowPlaying;

    $.jPlayer.timeFormat.showHour = true;
    $player.jPlayer({
        ended: function() {
            $nowPlaying.parent().find('.player-control').addClass('hide');
            $nowPlaying.parent().next().find('.player-time').addClass('hide');
            $nowPlaying.removeClass('hide');
        },
        cssSelectorAncestor: '#cdrList',
        supplied: 'oga, mp3',
        wmode: 'window',
        errorAlerts:true
    });

    $('.player-start').on('click', function() {
        var $this = $(this);

        if ($nowPlaying) {
            $player.jPlayer('stop');
            $nowPlaying.parent().find('.player-control').addClass('hide');
            $nowPlaying.parent().next().find('.player-time').addClass('hide');
            $nowPlaying.removeClass('hide');
        }

        $nowPlaying = $this;

        $player.jPlayer('setMedia', {
            oga: $this.attr('data-oga'),
            mp3: $this.attr('data-mp3')
        });

        $player.jPlayer('play');

        $this.addClass('hide');
        $this.parent().find('.player-control').removeClass('hide');
        $this.parent().next().find('.player-time').removeClass('hide');
    });
});