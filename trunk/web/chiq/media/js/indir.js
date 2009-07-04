$(document).ready(function() {
    $(".calisan").click(function(){
        $(".kurulan").removeClass("selected");
        $(".calisan").addClass("selected");
        $(".calisanindir").show();
        $(".kurulanindir").hide();
    });
    $(".kurulan").click(function(){
        $(".calisan").removeClass("selected");
        $(".kurulan").addClass("selected");
        $(".calisanindir").hide();
        $(".kurulanindir").show();
    });
});
