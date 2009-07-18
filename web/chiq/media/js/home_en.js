function kutusec(kutu){
    if (kutu == 1) $("#kutu1").attr("src", "/media/resimler/kutu/metin_kurumsal02.png");
    else $("#kutu1").attr("src", "/media/resimler/kutu/metin_kurumsal01.png");
    if (kutu == 2) $("#kutu2").attr("src", "/media/resimler/kutu/metin_bireysel02.png");
    else $("#kutu2").attr("src", "/media/resimler/kutu/metin_bireysel01.png");
    if (kutu == 3) $("#kutu3").attr("src", "/media/resimler/kutu/metin_gelistirici02.png");
    else $("#kutu3").attr("src", "/media/resimler/kutu/metin_gelistirici01.png");
    if (kutu == 4) $("#kutu4").attr("src", "/media/resimler/kutu/metin_cozumortaklari02.png");
    else $("#kutu4").attr("src", "/media/resimler/kutu/metin_cozumortaklari01.png");
}
$(document).ready(function() {
    $("#kutu1").mouseover(function(){
        $(".kutuic").css("background-image","url(/media/resimler/kutu/corporate.png)");
        kutusec(1);
    });
    $("#kutu2").mouseover(function(){
        $(".kutuic").css("background-image","url(/media/resimler/kutu/enduser.png)");
        kutusec(2);
    });
    $("#kutu3").mouseover(function(){
        $(".kutuic").css("background-image","url(/media/resimler/kutu/developer.png)");
        kutusec(3);
    });
    $("#kutu4").mouseover(function(){
        $(".kutuic").css("background-image","url(/media/resimler/kutu/partner.png)");
        kutusec(4);
    });
});
