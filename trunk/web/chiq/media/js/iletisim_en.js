$(document).ready(function() {
    $(".soru_sorun_secici").click(function(){
        $(".kurumsal_secici").removeClass("iletisim_secili");
        $(".soru_sorun_secici").addClass("iletisim_secili");
        $(".sirket_alani").hide();
        $("#ok").css("margin-left", "170px");
        $(".iletisim_aciklama_baslik").text("For your personal questions");
        $(".iletisim_aciklama_metin").text("You can ask your personal questions using here");
    });
    $(".kurumsal_secici").click(function(){
        $(".soru_sorun_secici").removeClass("iletisim_secili");
        $(".kurumsal_secici").addClass("iletisim_secili");
        $(".sirket_alani").show();
        $("#ok").css("margin-left", "60px");
        $(".iletisim_aciklama_baslik").text("For your enterprise questions");
        $(".iletisim_aciklama_metin").text("You can ask your enterprise questions using here.");
    });
});
