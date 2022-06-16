<?php
include_once('TextRankFacade.php');
include_once('StopWords/Vietnamese.php');
include_once('Tool/Parser.php');

header('Content-Type: application/json');

$text = $_POST['text'];

$tr = new TextRankFacade();

$stopWords = new Vietnamese();
$tr->setStopWords($stopWords);

// Array of the sentences from the most important part of the text:
$result = $tr->getHighlights($text); 

echo json_encode($result);
?>