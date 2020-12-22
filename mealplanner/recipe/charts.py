from pychartjs import BaseChart, ChartType, Color, Options

class ingredientsChart(BaseChart):
    type = ChartType.Doughnut

    class options:
        title = Options.Title("Price Breakdown")
        _labels = Options.Legend_Labels(fonColor=Color.Gray, fullwidth=False)
        legend = Options.Legend(position='bottom', labels=_labels)


class nutrientsChart(BaseChart):
    type = ChartType.Bar

    class options:
        title = Options.Title("Percentage of Daily Needs for Each Nutrient")
        _labels = Options.Legend_Labels(fonColor=Color.Gray, fullwidth=False)
        legend = Options.Legend(position='bottom', labels=_labels)