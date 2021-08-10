var search = () => {
    var name = $("#searchInput").val();

    if (name == "") {
        alert("검색할 선수명을 입력해 주세요.");
        return;
    }

    location.href = "../../playerSearch/" + name;
}

$("#searchInput").keypress((e) => {
    if (e.which == 13) {
        search();
    }
});

$("#search").click(() => {
    search();
});