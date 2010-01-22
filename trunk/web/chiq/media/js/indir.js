$(document).ready(function() {
    $(".calisan").click(function(){
        $(".kurulan").removeClass("selected");
        $(".calisan").addClass("selected");
        $(".calisanindir").show();
        $(".kurulanindir").hide();
        $(".ustaciklama").text("");
    });
    $(".kurulan").click(function(){
        $(".calisan").removeClass("selected");
        $(".kurulan").addClass("selected");
        $(".calisanindir").hide();
        $(".kurulanindir").show();
        $(".ustaciklama").text("Bir sürüm seçin.");
    });
});
