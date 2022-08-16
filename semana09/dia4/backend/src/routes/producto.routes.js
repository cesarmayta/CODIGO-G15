const {Router} = require('express');
const router = Router();

const {getAll} = require('../controllers/producto.controllers');

router.route('/')
    .get(getAll)


module.exports = router;