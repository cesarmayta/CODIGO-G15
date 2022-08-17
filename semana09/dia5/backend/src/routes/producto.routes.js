const {Router} = require('express');
const router = Router();

const {getAll,create,uploadImageAndCreate} = require('../controllers/producto.controllers');

router.route('/')
    .get(getAll)
    .post(create)

router.route('/upload')
    .post(uploadImageAndCreate)


module.exports = router;