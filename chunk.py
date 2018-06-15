import re
def chunked(sentence):
    sent_remind = re.search('[rR]emind',sentence)
    sent_reminder = re.search('[rR]eminder',sentence)
    try:
        if sent_remind:
            length = sent_remind.end()
        if sent_reminder:
            length = sent_reminder.end()
        if sent_remind or sent_reminder:
            sent_to = re.search('to ',sentence[length:])
            sent_for = re.search('for ',sentence[length:])
            sent_of = re.search('of ',sentence[length:])
            sent_about = re.search('about ', sentence[length:])
            sent_at = re.search('at ',sentence[length:])
            sent_on =re.search('on ',sentence[length:])
            sent_n = re.search('\n',sentence[length:])
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
            sent_at = re.search('at ',sentence[length+min_length:])
            sent_after = re.search('after ', sentence[length + min_length:])
            sent_by = re.search('by ',sentence[length+min_length:])
            sent_dot = re.search("\...", sentence[length + min_length:])
            sent_on = re.search('on ',sentence[length+min_length:])
            sent_every = re.search('every ',sentence[length+min_length:])
            sent_Date = re.search('Date:',sentence[length+min_length:])
            sent_slash = re.search('/', sentence[length + min_length:])
            if sent_every:
                sent_to_found.append(sent_every.start())
                not_found = False
            if sent_dot:
                sent_to_found.append(sent_dot.end())
                not_found = False
            if sent_at:
                sent_to_found.append(sent_at.start())
                not_found = False
            if sent_after:
                sent_to_found.append(sent_after.start())
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

            max_length = min(sent_to_found)
            return sentence[length + min_length:length + min_length + max_length]
    except AttributeError:
        pass

