const $elem = $('#gen');
function changep(){
    $elem.html('Loading HDF5 Model...')
    setTimeout(function (){$elem.html('Generating Elements...')}, 10000)
    setTimeout(function (){$elem.html('Writing MIDI File...')}, 15000)
    setTimeout(function (){$elem.html('Preparing to export...')}, 20000)
}
function post_req(btn) {
    let data = {'genre': `${btn}`}
    $('button').attr('disabled',true)
    changep()
    $.ajax({
        type: "POST",
        url: 'midi_gen',
        data: JSON.stringify(data),
        contentType: 'application/json;charset=UTF-8',
    })
        .done(function (filename){
            window.location.replace(`/export?filename=${filename}`)
            $elem.html('Click any of these buttons to generate a MIDI file...')
            $('button').removeAttr('disabled')
        })
}