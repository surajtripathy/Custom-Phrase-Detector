import re
def chunked(sentence):
    sent_remind = re.search('[rR]emind ',sentence)
    try:
        sent_to = re.search('to ',sentence[sent_remind.end():])
        sent_for = re.search('for ',sentence[sent_remind.end():])
        sent_of = re.search('of ',sentence[sent_remind.end():])
        sent_about = re.search('about ', sentence[sent_remind.end():])
        sent_at = re.search('at ',sentence[sent_remind.end():])
        sent_on =re.search('on ',sentence[sent_remind.end():])
        sent_n = re.search('\n',sentence[sent_remind.end():])
        sent_found = []
        found_true = False
        if sent_to:
            sent_found.append(sent_to.end())
            found_true = True
        if sent_on:
            sent_found.append(sent_on.end())
            found_true = True
        if sent_about:
            sent_found.append(sent_about.end())
            found_true = True
        if sent_for:
            sent_found.append(sent_for.end())
            found_true = True
        if sent_at:
            sent_found.append(sent_at.end())
            found_true = True
        if sent_of:
            sent_found.append(sent_of.end())
            found_true = True
        if found_true == False:
            sent_found.append(0)
        min_length = min(sent_found)
        sent_to_found = []
        not_found = True
        sent_at = re.search('at ',sentence[sent_remind.end()+min_length:])
        sent_by = re.search('by ',sentence[sent_remind.end()+min_length:])
        sent_dot = re.search("\...", sentence[sent_remind.end() + min_length:])
        sent_for = re.search('for ',sentence[sent_remind.end()+min_length:])
        sent_on = re.search('on ',sentence[sent_remind.end()+min_length:])
        sent_about = re.search('about ', sentence[sent_remind.end() + min_length:])
        sent_every = re.search('every ',sentence[sent_remind.end()+min_length:])
        sent_Date = re.search('Date:',sentence[sent_remind.end()+min_length:])
        sent_slash = re.search('/', sentence[sent_remind.end() + min_length:])
        if sent_every:
            sent_to_found.append(sent_every.start())
            not_found = False
        if sent_dot:
            sent_to_found.append(sent_dot.end())
            not_found = False
        if sent_at:
            sent_to_found.append(sent_at.start())
            not_found = False
        if sent_by:
            sent_to_found.append(sent_by.start())
            not_found = False
        if sent_slash:
            sent_to_found.append(sent_slash.start())
            not_found = False
        if sent_on:
            sent_to_found.append(sent_on.start())
            not_found = False
        if sent_Date:
            sent_to_found.append(sent_Date.start())
            not_found = False

        if not_found == True:
            sent_to_found.append(sent_n.start()-min_length)

        length = min(sent_to_found)
        return sentence[sent_remind.end() + min_length:sent_remind.end() + min_length + length]
    except AttributeError:
        pass






