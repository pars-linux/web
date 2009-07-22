$(document).ready(function() {
    $(".calisan").click(function(){
        $(".kurulan").removeClass("selected");
        $(".calisan").addClass("selected");
        $(".calisanindir").show();
        $(".kurulanindir").hide();
        $(".ustaciklama").text("Live CD will be announced soon.");
    });
    $(".kurulan").click(function(){
        $(".calisan").removeClass("selected");
        $(".kurulan").addClass("selected");
        $(".calisanindir").hide();
        $(".kurulanindir").show();
        $(".ustaciklama").text("Pick a download.");
    });
});
