//SKU GENERATE on Selleer
$(document).ready(function () {

    const charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let sku = 'SKU-' + '';
    for (let i = 0; i < 8; i++) {
        sku += charset.charAt(Math.floor(Math.random() * charset.length));
    }
    $('#generate-sku').val(sku);
});

$('.rtext').richText();
$('.rtext2').richText();
