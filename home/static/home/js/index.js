const quoteOfTheDayArray = [
    "Click wisely or suffer the consequences. Server bills aren't cheap, you know.",
    "My website, my rules. And the only rule for this site is -- no nginx",
    "Caution: sarcasm ahead. Proceed with a sense of humor or exit immediately.",
    "This website is like a rollercoaster ride through the mind of a mad coder.",
    "You can literally do much better in life than wasting your time on my website.",
    "505 is a good music, 404 is a timely error, 69 is good position, 37 is weird number",
    "Hands off the Inspect Element!"
]


const randomIndex = Math.floor(Math.random() * quoteOfTheDayArray.length);
$('#quote-of-day').text(quoteOfTheDayArray[randomIndex]);


