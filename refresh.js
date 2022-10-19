function refresh() {
    var TBA_STRING = "https://www.thebluealliance.com/api/v3/";
    var STB_STRING = "https://api.statbotics.io/v1/";

    function tbaCall(suffix) {
        var options = {
            "headers": {"X-TBA-Auth-Key": "5fsqBdP8JZfu5wzuBz00HpunpuNGbNiqquVIOuHGXPinm9uC7A564QjNB3m8dJ1z"} //throwaway key :)
        };
        var response = UrlFetchApp.fetch(TBA_STRING + suffix, options);
        return JSON.parse(response.getContentText());
    }

    function stbCall(suffix) {
        var response = UrlFetchApp.fetch(STB_STRING + suffix);
        return JSON.parse(response.getContentText());
    }

    function getTeamList(eventKey) {
        raw = tbaCall("event/" + eventKey + "/teams/keys");
        var teamList = [];
        for (var i = 0; i < raw.length; i++) {
            teamList.push(raw[i].substring(3));
        }
        return teamList;
    }

    function getTeamName(teamNumber) {
        raw = tbaCall("team/frc" + teamNumber);
        return raw.nickname;
    }

    function getRecentElo(teamNumber) {
        try {
            raw = stbCall("team/" + teamNumber);
            return raw[0].elo_recent;
        }
        catch(TypeError) {
            return 1500
        }
    }

    function getChairmansCount(teamNumber) {
        raw = tbaCall("team/frc" + teamNumber + "/awards");
        var count = 0;
        for (var i = 0; i < raw.length; i++) {
            if (raw[i].award_type == 0) {
                count++;
            }
        }
        return count;
    }

    function getTotalBanners(teamNumber) {
        raw = tbaCall("team/frc" + teamNumber + "/awards");
        var count = 0;
        for (var i = 0; i < raw.length; i++) {
            if (raw[i].award_type == 1 | raw[i].award_type == 0) {
                count++;
            }
        }
        return count;
    }

    //Columns:
    //team number (pulled from event list, TBA)
    //team name (pulled from team info, TBA)
    //team recent elo (pulled from team stats, STB)
    //team chairman's banners (pulled from team awards, TBA)
    //team total banners (pulled from team awards, TBA)

    // setup
    var spreadsheet = SpreadsheetApp.getActive();
    spreadsheet.getRange('A3:E').clearContent();
    var eventKey = spreadsheet.getRange('C1:C1').getValue()

    //iterate through team list
    var teamList = getTeamList(eventKey)
    Logger.log(teamList)
    Logger.log(Boolean((!teamList.includes("862"))))
    if (!teamList.includes("862")) {
      teamList.push(862)
    }
    for(var i=0;i<teamList.length;i++) {
        var data = [[teamList[i], getTeamName(teamList[i]), getRecentElo(teamList[i]), getChairmansCount(teamList[i]), getTotalBanners(teamList[i])]];
        Logger.log(i+3)
        spreadsheet.getRange("A" + (i+3) + ":E" + (i+3)).setValues(data);
    }
    var date = Utilities.formatDate(new Date(), "GMT-4", "MM/dd/yyyy HH:mm")
    spreadsheet.getRange('F1:F1').setValue(date)

};