<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "harirajanctc@gmail.com"; // <-- replace with your email address
    $from = $_POST["email"];
    $message = htmlspecialchars($_POST["message"]);
    $subject = "New Message from Zone Creators Bot";

    $body = "From: $from\n\nMessage:\n$message";

    $headers = "From: $from" . "\r\n" .
               "Reply-To: $from" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();

    if (mail($to, $subject, $body, $headers)) {
        echo "Message sent successfully.";
    } else {
        echo "Failed to send message. Please try again.";
    }
} else {
    echo "Invalid Request.";
}
?>
