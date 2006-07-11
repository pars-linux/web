<?php

    include_once 'config.php';

    class Pardus {

        var $Connection;

        function Pardus($DbHost,$DbUser,$DbPass,$DbData){
            if ($this->Connection=mysql_connect($DbHost,$DbUser, $DbPass))
                mysql_select_db($DbData,$this->Connection);
            else {
                echo("MySQL Connection Error, Check your settings. Error : ".mysql_error());
                die();
                return 0;
            }
        }

        function GetNewsList(){
            $query = "SELECT ID,Title,Date FROM News ORDER BY DATE DESC LIMIT 5";
            $result= mysql_query($query,$this->Connection);
            while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) {
                printf("<a href='#' onClick='get_news(%s);'> %s - %s </a><br>", $row["ID"],$row["Date"], $row["Title"]);
            }
            mysql_free_result($result);
        }

        function Search($Que) {
            $Que = mysql_escape_string($Que);
            $query = "SELECT Title,NiceTitle,Content,MATCH(Title, Content) AGAINST ('$Que') AS Score FROM Pages WHERE MATCH(Title, Content) AGAINST ('$Que') ORDER BY Score DESC";
            return $this->MakeArray(mysql_query($query,$this->Connection));
        }

        function GetNews($ID=""){
            if ($ID<>"")
                $query = "SELECT * FROM News WHERE ID=$ID";
            else
                $query = "SELECT * FROM News ORDER BY DATE DESC LIMIT 1";
            $result= mysql_query($query,$this->Connection);
            while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) {
                printf("<b>%s - %s</b><br> %s", $row["Date"], $row["Title"], $row["Content"]);
            }
            mysql_free_result($result);
        }

        function GetPage($NiceTitle="Main",$Parent){
            $query = "SELECT * FROM Pages WHERE NiceTitle='$NiceTitle' AND Parent='$Parent'";
            $result = mysql_query($query,$this->Connection);
            return (mysql_fetch_array($result, MYSQL_ASSOC));
        }

        function GetNiceTitles($ActivePage="") {
            $ActivePage =="" ? $Add ="" : $Add = " WHERE Parent='$ActivePage'";
            $query = "SELECT NiceTitle FROM Pages".$Add;
            return $this->MakeArray(mysql_query($query,$this->Connection),'NiceTitle');
        }

        function MakeArray($Raw,$Field="") {
            $i=0;
            while ($Row = mysql_fetch_array($Raw)) {
                $Field == "" ? $ReturnValue[$i] = $Row : $ReturnValue[$i] = $Row[$Field];
                $i++;
            }
            if ($i==0)
                $ReturnValue = 0;
            mysql_free_result($Raw);
            return $ReturnValue;
        }
    }

    function turnToEn($Data,$Reverse){
        mb_regex_encoding('utf-8');
        $TR = Array ('İ','Ş','Ğ','Ö','Ü','Ç','ı','ş','ğ','ö','ü','ç');
        $EN = Array ('I','S','G','O','U','C','i','s','g','o','u','c');
        for ($i=0; $i<sizeof($TR); $i++) {
            if ($Reverse)
                $Data = mb_ereg_replace($EN[$i],$TR[$i],$Data);
            else
                $Data = mb_ereg_replace($TR[$i],$EN[$i],$Data);
        }
        return $Data;
    }

    function GetPos($Data,$Word) {
        return mb_strpos(mb_strtolower($Data,'UTF-8'),mb_strtolower($Word,'UTF-8'),0,'UTF-8'); 
    }

    function GetHighlighted($Word,$Data,$Color) {
        $Return = mb_ereg_replace($Word,"<b>".$Word."</b>",$Data);
        $Return = mb_ereg_replace(turnToEn($Word,0),"<b>".turnToEn($Word,0)."</b>",$Return);
        return $Return;
    }

    function Highlight($Data,$Word,$Score,$Size=260,$Color="yellow") {
        $Data       = strip_tags($Data);
        $TempData   = mb_strtolower($Data,'UTF-8');

        $RawWord    = split(" ",$Word);
        $Size       = round ($Size/sizeof($RawWord));
        foreach($RawWord as $Word) {
            $Word       = strip_tags($Word);
            $TempWord   = mb_strtolower($Word,'UTF-8');
            # I know it sucks.
            $Pos        = GetPos($TempData,$TempWord);
            if ($Pos==0){
                $Pos    = GetPos($TempData,turnToEn($TempWord,0));
                $EnWord = turnToEn($TempWord,0);
            }
            if ($Pos==0){
                $Pos    = GetPos($TempData,turnToEn($TempWord,1));
                $TrWord = turnToEn($TempWord,1);
            }
            $Piece     .= "....".mb_substr($Data,$Pos,$Size,'UTF-8');
        }

        $IData      = mb_strtolower($Piece,'UTF-8');
        foreach ($RawWord as $Word) {
            $IWord      = mb_strtolower($Word,'UTF-8');
            $IData      = GetHighlighted($IWord,$IData,$Color);
        }
        return $IData;
    }

    if ($_GET["NewsID"]<>""){
        $Pardus = new Pardus($DbHost,$DbUser,$DbPass,$DbData);
        $Pardus->GetNews($_GET["NewsID"]);
    }

    
?>
