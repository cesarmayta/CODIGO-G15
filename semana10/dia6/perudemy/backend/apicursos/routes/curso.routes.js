const {Router} = require('express');
const router = Router();

const {verifyToken} = require('../middlewares/auth.handler');

const {getAll,getById} = require('../controllers/curso.controllers');

router.route('/')
    .get(getAll)

router.route('/:id')
    .get(verifyToken,getById)

module.exports = router;