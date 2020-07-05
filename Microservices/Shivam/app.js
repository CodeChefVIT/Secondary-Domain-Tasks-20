const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const router = express.Router();
//===============================================

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(router);
//===============================================

//routes that handle requests
//=========================================
router.get("/add", (req, res) => {
	const sum = req.body.one + req.body.two;
	res.status(200).json({
		addition: sum,
	});
});
router.get("/delete", (req, res) => {
	const del = req.body.one - req.body.two;
	res.status(200).json({
		deletion: del,
	});
});
router.get("/multiply", (req, res) => {
	const prod = req.body.one * req.body.two;
	res.status(200).json({
		product: prod,
	});
});
router.get("/divide", (req, res) => {
	const div = req.body.one / req.body.two;
	res.status(200).json({
		division: div,
	});
});

//=========================================

app.use((req, res, next) => {
	const error = new Error("Request Not found sorry!");
	error.status = 404;
	next(error);
});

app.use((error, req, res, next) => {
	res.status(error.status || 500);
	res.json({
		error: {
			message: error.message,
		},
	});
});

const PORT = 3000;

app.listen(PORT, () => {
	console.log(`Listening on port ${PORT}`);
});
