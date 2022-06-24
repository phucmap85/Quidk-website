<?php
    require_once('vendor/autoload.php');
    include_once('TextRank/TextRankFacade.php');
    include_once('TextRank/StopWords/Vietnamese.php');
    include_once('TextRank/StopWords/English.php');
    include_once('TextRank/Tool/Parser.php');
    header('Content-Type: application/json; charset=utf-8');

    $url = $_POST['text'];

    $content = file_get_contents($url);

    $dom = new domDocument();
    @$dom->loadHTML(mb_convert_encoding($content, 'HTML-ENTITIES', 'UTF-8'));

    $scrape = $dom->getElementsByTagName('p');

    $text = "";
    foreach($scrape as $p) {
        $text .= $p->nodeValue;
        $text .= ' ';
    }

    $tr = new TextRankFacade();

    $detector = new LanguageDetector\LanguageDetector(null, ['en', 'vi']);

    $lang = $detector->evaluate($text);

    $stopWords = new Vietnamese();
    if($lang == 'en') $stopWords = new English();

    $tr->setStopWords($stopWords);
    $result = $tr->getHighlights($text);

    echo json_encode($result);
?>