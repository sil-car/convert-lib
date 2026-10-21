# https://github.com/sillsdev/FieldWorks/blob/ba50e637df9593a2a972b29bf670226e89c0a21b/Lib/src/Converter/Convertlib/Convert.cs

from .classes import Classes
from .rtclass import RTClass


# Stream reader that will change control charaters to spaces. Will prevent
# conversion of projects with control characters in the text from failing.
# Could quote the characters, but they are not likely to be really wanted in
# the text.
class FilteredStreamReader():
    pass


class Convert:
    def __init__(self):
        self.m_file_name = ""
        self.m_model_name = ""
        self.node_value = 0
        self.hold_class_num = 0
        self.node_class = ""
        self.hold_node = ""
        self.hold_class_name = ""
        self.hold_version = ""
        self.start_class = False
        self.start_elem = False
        self.closed_elem = False
        self.custom_flag = False
        self.preserve_space = False
        self.guid_stack = []
        self.o_ord_list = dict()
        self.custom_list = []
        self.elem_dentry = []
        self.stack_elements = []
        self.stack_classes = []
        self.list_classes = []
        self.current_rt = RTClass()
        self.lang_proj_class = RTClass()
        self.h_class = Classes()
        self.class_list = dict()
        self.mod_list = dict()
        self.dic_class = dict()

    def conversion(self):
        pass
