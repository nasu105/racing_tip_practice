import pandas as pd

url = "https://db.netkeiba.com/race/201901010101"
pd.read_html(url)[0]

# 場所コード
# 01:札幌, 02:函館, 03:福島, 04:新潟, 05:東京, 06:中山, 07:中京, 08:京都, 09:阪神, 10:小倉

def scrape_race_results(race_id_list):
  # 辞書としてrace_resultsを初期化
  race_results = {}
  for race_id in race_id_list:
    url = 'https://db.netkeiba.com/race/' + race_id
    # race_idをキーとして結果を辞書に格納
    race_results[race_id] = pd.read_html(url)[0]
  return race_results

# レースIDのリスト
race_id_list = ["201902010101", "201902010102", "201902010103"]

# 関数をテスト
test = scrape_race_results(race_id_list)
