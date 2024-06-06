from utilities.functions.get.get_survey import get_survey
from utilities.functions.get.get_question import get_question
from utilities.functions.get.get_flow import get_flow
from utilities.functions.get.get_block import get_block
from utilities.functions.get.get_options import get_options

from utilities.functions.put.put_question import put_question
from utilities.functions.put.put_question import put_question
from utilities.functions.put.put_options import put_options
from utilities.functions.put.put_flow import put_flow

from utilities.functions.put.put_block import put_block
from utilities.functions.post.publish_survey import publish_survey

from utilities.get_headers import get_headers

headers = get_headers()

# get_question("top_gender", headers)

# put_question("average", headers)
# put_block("main", headers)
# get_block("main", headers)
# get_flow(headers)
# put_flow(headers)

get_survey(headers)

# put_options(headers)
publish_survey(headers)
