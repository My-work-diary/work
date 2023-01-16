$(document).ready(function () {
    show_goal();
});
var testnum=0;
function save_goal() {
    let day = $('#day').val()
    let title = $('#title').val()
    let goal_num = $('#goal_num').val()
    let goal_set = $('#goal_set').val()
    testnum = testnum+1
    console.log(testnum)
    $.ajax({
        type: "POST",
        url: "/goal",
        data: {day_give: day, title_give: title, goal_num_give: goal_num, goal_set_give: goal_set},
        success: function (response) {
            let check = response['check']
            if (check == 1) {
                alert("입력 완료")
                window.location.reload()
            } else if (check == 0) {
                alert("중복된 값입니다. 요일과 운동명을 확인하세요")
            }
        }
    });
}

function show_goal() {
    $.ajax({
        type: "GET",
        url: "/goal",
        data: {},
        success: function (response) {
            let rows = response['goals']
            for (let i = 0; i < rows.length; i++) {
                let num = rows[i]['num']
                let day = rows[i]['day']
                let title = rows[i]['title']
                let goal_num = rows[i]['goal_num']
                let goal_set = rows[i]['goal_set']
                let temp_html = ``

                temp_html = `<li>
                               ${change_day(day)} ${change_title(title)}  ${goal_num}회 ${goal_set}세트
                                <button onclick="delete_goal(${num})" type="button" >삭제</button>
                    <!--        <button onClick="update_bucket(${num})" type="button" >수정</button>-->
                            </li>   `
                    $('#goal_list').append(temp_html)
            }
        }
    });
}

function change_day(day) {
    if (day == 'mon') {
        day = day.replace('mon', '월요일');
    } else if (day == 'tue') {
        day = day.replace('tue', '화요일');
    } else if (day == 'wed') {
        day = day.replace('wed', '수요일');
    } else if (day == 'thu') {
        day = day.replace('thu', '목요일');
    }else if (day == 'fri') {
        day = day.replace('fri', '금요일');
    } else if (day == 'sat') {
        day = day.replace('sat', '토요일');
    } else {
        day = day.replace('sun', '일요일');
    }
    return day
}

function change_title(title) {
    if (title == 'squat') {
        title = title.replace('squat', '스쿼트');
    } else if (title == 'lunge') {
        title = title.replace('lunge', '런지');
    } else if (title == 'pull') {
        title = title.replace('pull', '풀업');
    } else if (title == 'push') {
        title = title.replace('push', '푸쉬업');
    } else {
        title = title.replace('sit', '윗몸 일으키기');
    }
    return title
}

function delete_goal(num) {
        $.ajax({
                type: "POST",
                url: "/goal/delete",
                data: {'num_give': num,'title_give':title},
                success: function (response) {
                    alert("삭제 완료")
                    window.location.reload()
                }
            });
    }

