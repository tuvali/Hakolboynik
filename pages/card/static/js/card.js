function validateForm() {
    var exMonth = document.getElementById('mm-card').value;
    var exYear = document.getElementById('year-card').value;
    var date = new Date();
    var month = date.getMonth()+1;
    var year = date.getFullYear();
    var twoDigitYear = year.toString().substr(-2);
    console.log(exMonth);
    console.log(exYear);
    console.log(month);
    console.log(twoDigitYear);
    console.log(year);
    if (twoDigitYear > exYear || (twoDigitYear === exYear && month >= exMonth)) {
        alert("כרטיס האשראי שהוזן פג תוקף, אנא הזן תאריך תקין");
        return window.location.href='/card';
    }
    else{
        alert("תשלום התקבל בהצלחה!");
        return window.location.href='/order_received';
    }

}
