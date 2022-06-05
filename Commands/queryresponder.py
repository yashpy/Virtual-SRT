import audioprocessor as ap
import querycommands as qc
import browsercommands as bc
import utilitycommands as uc


def queryResponder(request_input, answers):
    if(request_input['type'] == 'text_queries'):
        answer = answers[request_input['index']]
        reply = answer.replace(
            "{assistantName}", request_input['assistantName'])
        reply = reply.replace(
            "{userName}", request_input['userName'])
        ap.say(reply)
        qc.queryCommands(request_input['text'])
        bc.browserCommands(request_input['text'], answer)
        uc.utilityCommands(request_input['text'])

    elif(request_input['type'] == 'command_queries'):
        answer = answers[request_input['index']]
        ap.say(answer)
        qc.queryCommands(request_input['text'])

    elif(request_input['type'] == 'browser_queries'):
        answer = answers[request_input['index']]
        bc.browserCommands(request_input['text'], answer)

    else:
        ap.say('Sorry, i didn\'t get ' + request_input['text'])
