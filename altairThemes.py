# Altair themes
# By
# Gregory W. Schwartz

'''
Use:

sys.path.append("/path/to/parent/directory/of/altairThemes.py")

if True:  # In order to bypass isort when saving
    import altairThemes

# register the custom theme under a chosen name
alt.themes.register("publishTheme", altairThemes.publishTheme)

# enable the newly registered theme
alt.themes.enable("publishTheme")
'''

import altair as alt


def publishTheme():
    # Typography
    font = "Arial"
    labelFont = "Arial"
    sourceFont = "Arial"
    fontSize = 10.66670036  # Size 8pt for publishing

    # Axes
    axisColor = "#000000"

    return {
        "config": {
            "view": {
                "height": 80,  # Customize for appropriate size
                "width": 100,  # Customize for appropriate size
                "strokeOpacity": 0,  # Despine
                "strokeWidth": 0.756,
            },
            "style": {
                "guide-title": {
                    "fontSize": fontSize
                },
                "guide-label": {
                    "fontSize": fontSize
                }
            },
            "title": {
                "fontSize": fontSize,
                "font": font,
                "fontColor": "#000000",
                "fontWeight": "normal",
            },
            "axis": {
                "domainColor": "#000000",
                "domainWidth": 0.756,
                "grid": False,
                "gridWidth": 0.756,
                "labelAngle": 0,
                "labelFont": labelFont,
                "labelFontSize": fontSize,
                "tickColor": axisColor,
                "tickWidth": 0.756,
                "titleFont": font,
                "titleFontSize": fontSize,
                "titleFontWeight": "normal",
            },
            # For individual axis
            # "axisX": {
            #     "grid": False,
            #     "domainColor": "#000000",
            #     "labelFont": labelFont,
            #     "labelFontSize": fontSize,
            #     "labelAngle": 0,
            #     "tickColor": axisColor,
            #     "titleFont": font,
            #     "titleFontSize": fontSize,
            #     "titleFontWeight": "normal",
            # },
        }
    }
