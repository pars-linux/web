$(document).ready(function() {
    $(".calisan").click(function(){
        $(".kurulan").removeClass("selected");
        $(".calisan").addClass("selected");
        $(".calisanindir").show();
        $(".kurulanindir").hide();
        $(".ustaciklama").text("Çalışan CD sürümümüz yakında yayınlanacaktır.");
    });
    $(".kurulan").click(function(){
        $(".calisan").removeClass("selected");
        $(".kurulan").addClass("selected");
        $(".calisanindir").hide();
        $(".kurulanindir").show();
        $(".ustaciklama").text("Bir sürüm seçin.");
    });
});
