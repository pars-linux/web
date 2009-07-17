$(document).ready(function() {
    $(".soru_sorun_secici").click(function(){
        $(".kurumsal_secici").removeClass("iletisim_secili");
        $(".soru_sorun_secici").addClass("iletisim_secili");
        $(".sirket_alani").hide();
        $(".iletisim_aciklama_baslik").text("Bireysel sorularınız için");
        $(".iletisim_aciklama_metin").text("Bireysel sorularınızı buradan sorabilirsiniz");
    });
    $(".kurumsal_secici").click(function(){
        $(".soru_sorun_secici").removeClass("iletisim_secili");
        $(".kurumsal_secici").addClass("iletisim_secili");
        $(".sirket_alani").show();
        $(".iletisim_aciklama_baslik").text("Kurumsal sorularınız için");
        $(".iletisim_aciklama_metin").text("Kurumsal sorularınızı buradan sorabilirsiniz");
    });
});