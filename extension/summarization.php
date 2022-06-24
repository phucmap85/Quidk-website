<?php
    require_once('vendor/autoload.php');
    include_once('TextRank/TextRankFacade.php');
    include_once('TextRank/Tool/Parser.php');
	
	include_once('TextRank/StopWords/Vietnamese.php');
    include_once('TextRank/StopWords/English.php');
	include_once('TextRank/StopWords/French.php');
	include_once('TextRank/StopWords/German.php');
	include_once('TextRank/StopWords/Indonesian.php');
	include_once('TextRank/StopWords/Italian.php');
	include_once('TextRank/StopWords/Norwegian.php');
	include_once('TextRank/StopWords/Russian.php');
	include_once('TextRank/StopWords/Spanish.php');
	
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

    $detector = new LanguageDetector\LanguageDetector(null, ['vi', 'en', 'fr', 'de', 'id', 'it', 'no', 'ru', 'es']);

    $lang = $detector->evaluate($text);

    $stopWords = new Vietnamese();
    if($lang == 'en') $stopWords = new English();
	if($lang == 'fr') $stopWords = new French();
	if($lang == 'de') $stopWords = new German();
	if($lang == 'id') $stopWords = new Indonesian();
	if($lang == 'it') $stopWords = new Italian();
	if($lang == 'no') $stopWords = new Norwegian();
	if($lang == 'ru') $stopWords = new Russian();
	if($lang == 'es') $stopWords = new Spanish();

    $tr->setStopWords($stopWords);
    $result = $tr->getHighlights($text);

    echo json_encode($result);
?>