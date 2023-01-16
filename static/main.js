function squat() {
    $.ajax({
        type: 'GET',
        url: '/youtube',
        data: {},
        success: function (response) {
            $('#show').empty();
            let rows = response['videos']
            for (let i = 0; i < rows.length; i++) {
                if (rows[i]['workName'] === 'squat') {
                    let url = rows[i]['url']

                    let temp_html = `<iframe src="${url}"></iframe>`

                    $('#show').append(temp_html)
                }
            }
            console.log(response)
        }
    })
}

function lunge() {
    $.ajax({
        type: 'GET',
        url: '/youtube',
        data: {},
        success: function (response) {
            $('#show').empty();
            let rows = response['videos']
            for (let i = 0; i < rows.length; i++) {
                if (rows[i]['workName'] === 'lunge') {
                    let url = rows[i]['url']

                    let temp_html = `<iframe src="${url}"></iframe>`

                    $('#show').append(temp_html)
                }
            }
            console.log(response)
        }
    })
}

function pulls() {
    $.ajax({
        type: 'GET',
        url: '/youtube',
        data: {},
        success: function (response) {
            $('#show').empty();
            let rows = response['videos']
            for (let i = 0; i < rows.length; i++) {
                if (rows[i]['workName'] === 'pulls') {
                    let url = rows[i]['url']

                    let temp_html = `<iframe src="${url}"></iframe>`

                    $('#show').append(temp_html)
                }
            }
            console.log(response)
        }
    })
}

function pushs() {
    $.ajax({
        type: 'GET',
        url: '/youtube',
        data: {},
        success: function (response) {
            $('#show').empty();
            let rows = response['videos']
            for (let i = 0; i < rows.length; i++) {
                if (rows[i]['workName'] === 'pushs') {
                    let url = rows[i]['url']

                    let temp_html = `<iframe src="${url}"></iframe>`

                    $('#show').append(temp_html)
                }
            }
            console.log(response)
        }
    })
}

function sit() {
    $.ajax({
        type: 'GET',
        url: '/youtube',
        data: {},
        success: function (response) {
            $('#show').empty();
            let rows = response['videos']
            for (let i = 0; i < rows.length; i++) {
                if (rows[i]['workName'] === 'sit') {
                    let url = rows[i]['url']

                    let temp_html = `<iframe src="${url}"></iframe>`

                    $('#show').append(temp_html)
                }
            }
            console.log(response)
        }
    })
}


function posting() {
    let url = $('#url').val()
    let workName = $('#workName').val()

    $.ajax({
        type: 'POST',
        url: '/youtube',
        data: {url_give: url, workName_give: workName},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
}