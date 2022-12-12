const express = require("express");
const app = express();

app.listen(process.env.PORT || 3000, () => {
  console.log("Application started and Listening on port 3000");
});

// server css as static
app.use(express.static(__dirname));


app.get("/", (req, res) => {
  res.sendFile(__dirname + "/results/index.html");
});

// app.post("/", (req, res) => {
//   console.log(req.body)
// });

app.get("/ldavis_total_2", (req, res) =>{
  res.sendFile(__dirname + "/results/ldavis_comment_total_2.html");
});

app.get("/ldavis_total_3", (req, res) =>{
  res.sendFile(__dirname + "/results/ldavis_comment_total_3.html");
});

app.get("/ldavis_total_4", (req, res) =>{
  res.sendFile(__dirname + "/results/ldavis_comment_total_4.html");
});

app.get("/ldavis_total_5", (req, res) =>{
  res.sendFile(__dirname + "/results/ldavis_comment_total_5.html");
});

app.get("/ldavis_total_6", (req, res) =>{
  res.sendFile(__dirname + "/results/ldavis_comment_total_6.html");
});

app.get("/ldavis_total_7", (req, res) =>{
  res.sendFile(__dirname + "/results/ldavis_comment_total_7.html");
});

app.get("/ldavis_total_8", (req, res) =>{
  res.sendFile(__dirname + "/results/ldavis_comment_total_8.html");
});

app.get("/ldavis_total_9", (req, res) =>{
  res.sendFile(__dirname + "/results/ldavis_comment_total_9.html");
});

