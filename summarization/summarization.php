<?php 
include_once('TextRankFacade.php');
include_once('StopWords/Vietnamese.php');
include_once('Tool/Parser.php');

header('Content-Type: application/json');

$text = $_POST['text'];

$tr = new TextRankFacade();

$stopWords = new Vietnamese();
$tr->setStopWords($stopWords);

// Array of the most important keywords:
$result = $tr->getOnlyKeyWords($text); 

// Array of the sentences from the most important part of the text:
$result = $tr->getHighlights($text); 

// Array of the most important sentences from the text:
$result = $tr->summarizeTextBasic($text);

echo $result;
?>
