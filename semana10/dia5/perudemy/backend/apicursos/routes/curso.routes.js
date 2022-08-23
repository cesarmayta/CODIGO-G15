const {Router} = require('express');
const router = Router();

const {getAll} = require('../controllers/curso.controllers');

router.route('/')
    .get(getAll)

module.exports = router;