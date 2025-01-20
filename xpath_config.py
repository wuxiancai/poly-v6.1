"""
XPATH配置文件
用于集中管理所有XPATH路径
修改XPATH时只需要在此文件中更新对应的值
"""

class XPathConfig:
    # 登录相关
    LOGIN_BUTTON = '//*[@id="__pm_viewport"]/nav[1]/div[1]/div[3]/div/nav/div/ul/div[1]/div/button'
    
    # 交易按钮
    SELL_BUTTON = '//*[@id="column-wrapper"]/div/div/div/div[1]/div/div[1]/div/div/div[2]' #可能需要改动
    BUY_BUTTON = '//*[@id="column-wrapper"]/div/div/div/div[1]/div/div[1]/div/div/div[1]' #可能需要改动
    BUY_YES_BUTTON = '//*[@id="column-wrapper"]/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div' #可能需要改动
    BUY_NO_BUTTON = '//*[@id="column-wrapper"]/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div' #可能需要改动
    SELL_YES_BUTTON = '//*[@id="column-wrapper"]/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div' #可能需要改动
    SELL_NO_BUTTON = '//*[@id="column-wrapper"]/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div' #可能需要改动
    BUY_CONFIRM_BUTTON = '//*[@id="column-wrapper"]/div/div/div/div[1]/div/div[2]/div[4]/button' #可能需要改动,买卖按钮是一样的
    SELL_PROFIT_BUTTON = '//*[@id="column-wrapper"]/div/div/div/div[1]/div/div[2]/div[4]/button' #可能需要改动，买卖按钮是一样的
    
    # 金额输入
    AMOUNT_INPUT = '//div[@class="c-dhzjXW c-dhzjXW-idAwKFA-css"]//input' #长期有效，可能需要改动
    
    # Position相关
    POSITION_YES_LABEL  = '//div[@class="c-dhzjXW c-chKWaB c-chKWaB-eVTycx-color-green c-dhzjXW-ibxvuTL-css" and text()="Yes"]' #长期有效
    POSITION_NO_LABEL = '//div[@class="c-dhzjXW c-chKWaB c-chKWaB-kNNGp-color-red c-dhzjXW-ibxvuTL-css" and text()="No"]' #长期有效
    POSITION_SELL_BUTTON = '//button[@class="c-gBrBnR c-gBrBnR-iifsICY-css"]' #长期有效
    POSITION_SELL_YES_BUTTON = '(//button[@class="c-gBrBnR c-gBrBnR-iifsICY-css"])[1]' #长期有效,不需要改动
    POSITION_SELL_NO_BUTTON = '(//button[@class="c-gBrBnR c-gBrBnR-iifsICY-css"])[2]' #长期有效,不需要改动
    
    # 价格相关
    YES_PRICE = '(//span[@class="c-bjtUDd c-bjtUDd-ijxkYfH-css"])[1]' #长期有效,不需要改动
    NO_PRICE = '(//span[@class="c-bjtUDd c-bjtUDd-ijxkYfH-css"])[2]' #长期有效,不需要改动
    PORTFOLIO_VALUE = '(//span[@class="c-PJLV c-jaFKlk c-PJLV-ibdakYG-css"])[1]' #长期有效,不需要改动
    CASH_VALUE = '(//span[@class="c-PJLV c-jaFKlk c-PJLV-ibdakYG-css"])[2]' #长期有效,不需要改动

     # Website按钮相关
    WEBSITE_BUY = BUY_BUTTON
    WEBSITE_SELL = SELL_BUTTON
    WEBSITE_BUY_CONFIRM = BUY_CONFIRM_BUTTON
    WEBSITE_SET_EXPIRATION = "//button[contains(text(), 'Set Expiration')]"
    WEBSITE_MODAL_BUY = "//div[contains(@class, 'modal')]//button[contains(text(), 'Buy')]"

    # 卖出相关
    SELL_POSITION_BUTTON = "//div[contains(text(), '{}')]/..//button[contains(text(), '卖出')]"
    CONFIRM_SELL_BUTTON = "//button[contains(text(), '确认卖出')]"

    # 价格监控相关
    PRICE_BUTTON = "//button[contains(@class, '{}')]"  # 将通过format填充yes/no

    # 买入yes/no时通过判断yes/no的值来判断是否买入成功
    POSITION_YES_VALUE = '//*[@id="event-detail-container"]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/span[2]'
    POSITION_NO_VALUE = '//*[@id="event-detail-container"]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/span[2]'

    # history相关
    HISTORY = '//*[@id="event-detail-container"]/div/div[2]/div/div[5]/div/div[2]/div/p'
    HISTORY_YES_VALUE = '//*[@id="event-detail-container"]/div/div[2]/div/div[5]/div/div[2]/div/p'
    HISTORY_NO_VALUE = '//*[@id="event-detail-container"]/div/div[2]/div/div[5]/div/div[2]/div/p'
