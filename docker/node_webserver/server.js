const express = require('express')
const app = express()
const path = require('path');
const PORT = 3000;
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + '/public/index.html'));
})

app.listen(PORT, () => console.log('Listening on port '+PORT))

process.on('SIGINT', function() {
    process.exit();
});