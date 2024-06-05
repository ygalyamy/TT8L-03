<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $book_rating = $_POST['book_rating'];
    $read_again = $_POST['read_again'];
    $impact_rating = $_POST['impact_rating'];
    $genre = $_POST['genre'];
    $overall_thoughts = $_POST['overall_thoughts'];

    // Process and save the data (e.g., save to a file, database, etc.)
    // For demonstration, we'll save the data to a text file
    $file = fopen("book_reviews.txt", "a");
    fwrite($file, "Book Rating: $book_rating\n");
    fwrite($file, "Read Again: $read_again\n");
    fwrite($file, "Impact Rating: $impact_rating\n");
    fwrite($file, "Genre: $genre\n");
    fwrite($file, "Overall Thoughts: $overall_thoughts\n");
    fwrite($file, "-------------------------\n");
    fclose($file);

    // Redirect to a thank you page (or you can display a message)
    header("Location: thank_you.html");
    exit();
}
?>
