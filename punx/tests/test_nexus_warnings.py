"""
issue 14: implement warnings as advised in NeXus manual

:see: http://download.nexusformat.org/doc/html/search.html?q=warning&check_keywords=yes&area=default

Actually, flag them as NOTE unless WARN is compelling
"""


def test_trivial():
    assert True

# import h5py
# import numpy
# import os
# import sys
# import tempfile
# import unittest

# _path = os.path.join(os.path.dirname(__file__), '..', 'src')
# if _path not in sys.path:
#     sys.path.insert(0, _path)


# class Warning__1(unittest.TestCase):
#     '''
#     whatever
#     '''

#     def setUp(self):
#         # create the test file
#         tfile = tempfile.NamedTemporaryFile(suffix='.hdf5', delete=False)
#         tfile.close()
#         self.hdffile = tfile.name
#         self.validator = None

#     def tearDown(self):
#         if self.validator is not None:
#             self.validator.close()
#             self.validator = None
#         os.remove(self.hdffile)
#         self.hdffile = None

#     def test_NXcollection_always_generates_a_warning(self):
#         '''
#         For NeXus validation, NXcollection will always generate a
#         warning since it is always an optional group.
#         Anything (groups, fields, or attributes) placed in an
#         NXcollection group will not be validated.
#         '''
#         self.assertTrue(True, 'tba')

#     def test_note_items_added_to_base_class_and_not_in_NXDL(self):
#         '''
#         Validation procedures should treat such additional
#         items (not covered by a base class specification)
#         as notes or warnings rather than errors.
#         '''
#         self.assertTrue(True, 'tba')

#     def test_NXDL_attribute__ignoreExtraAttributes(self):
#         '''
#         Only validate known attributes; do not not warn about unknowns.

#         The ignoreExtraAttributes attribute is a flag to the process of
#         validating NeXus data files. By setting ignoreExtraAttributes="true",
#         presence of any undefined attributes in this class will not generate
#         warnings during validation. Normally, validation will check all the
#         attributes against their definition in the NeXus base classes and
#         application definitions. Any items found that do not match the
#         definition in the NXDL will generate a warning message.
#         '''
#         self.assertTrue(True, 'tba')

#     def test_NXDL_attribute__ignoreExtraFields(self):
#         '''
#         Only validate known fields; do not not warn about unknowns.

#         The ignoreExtraFields attribute is a flag to the process of
#         validating NeXus data files. By setting ignoreExtraFields="true",
#         presence of any undefined fields in this class will not generate
#         warnings during validation. Normally, validation will check all
#         the fields against their definition in the NeXus base classes
#         and application definitions. Any items found that do not match
#         the definition in the NXDL will generate a warning message.
#         '''
#         self.assertTrue(True, 'tba')

#     def test_NXDL_attribute__ignoreExtraGroups(self):
#         '''
#         Only validate known groups; do not not warn about unknowns.

#         The ignoreExtraGroups attribute is a flag to the process of
#         validating NeXus data files. By setting ignoreExtraGroups="true",
#         presence of any undefined groups in this class will not generate
#         warnings during validation. Normally, validation will check all
#         the groups against their definition in the NeXus base classes and
#         application definitions. Any items found that do not match the
#         definition in the NXDL will generate a warning message.
#         '''
#         self.assertTrue(True, 'tba')

#     def test_naming_conventions__issue_65(self):
#         import punx.validate, punx.finding, punx.logs
#         punx.logs.ignore_logging()

#         # create the HDF5 content
#         hdf5root = h5py.File(self.hdffile, "w")
#         entry = hdf5root.create_group('entry')
#         entry.attrs['NX_class'] = 'NXentry'
#         data = entry.create_group('data')
#         data.attrs['NX_class'] = 'NXdata'
#         data.attrs['signal'] = 'valid_item_name_strict'
#         data.create_dataset('data', data=range(5))
#         entry.create_dataset('strict', data=range(5))
#         entry.create_dataset('Relaxed', data=range(5))
#         entry.create_dataset('not.allowed', data=range(5))
#         entry.create_dataset('also not allowed', data=range(5))
#         entry.create_dataset('_starts_with_underscore', data=range(5))
#         entry.create_dataset('0_starts_with_number', data=range(5))
#         entry.create_dataset('dataset_name_has@symbol', data=range(5))
#         entry.attrs['@@@'] = 'invalid'
#         entry.attrs['@attribute'] = 'invalid'
#         entry.attrs['attribute@'] = 'invalid'
#         hdf5root.close()

#         self.validator = punx.validate.Data_File_Validator(self.hdffile)
#         self.validator.validate()
#         all_findings = [str(f) for f in self.validator.findings]
#         # print('\n' + '\n'.join(all_findings) + '\n')

#         expected_findings = '''\
#         /entry/0_starts_with_number WARN: validItemName: valid HDF5 item name, not valid with NeXus
#         /entry/0_starts_with_number@units NOTE: field@units: does not exist
#         /entry/_starts_with_underscore OK: validItemName-strict: strict re: [a-z_][a-z0-9_]*
#         /entry/_starts_with_underscore@units NOTE: field@units: does not exist
#         /entry/Relaxed NOTE: validItemName: relaxed re: [A-Za-z_][\w_]*
#         /entry/Relaxed@units NOTE: field@units: does not exist
#         /entry/also not allowed WARN: validItemName: valid HDF5 item name, not valid with NeXus
#         /entry/also not allowed@units NOTE: field@units: does not exist
#         /entry/dataset_name_has@symbol WARN: validItemName: valid HDF5 item name, not valid with NeXus
#         /entry/not.allowed WARN: validItemName: valid HDF5 item name, not valid with NeXus
#         /entry/not.allowed@units NOTE: field@units: does not exist
#         /entry/strict OK: validItemName-strict: strict re: [a-z_][a-z0-9_]*
#         /entry/strict@units NOTE: field@units: does not exist
#         /entry@@@@ WARN: validItemName: valid HDF5 attribute name, not valid with NeXus
#         /entry@@attribute WARN: validItemName: valid HDF5 attribute name, not valid with NeXus
#         /entry@attribute@ WARN: validItemName: valid HDF5 attribute name, not valid with NeXus
#         '''.splitlines()

#         for f in expected_findings:
#             if len(f.strip()) > 0:
#                 # print('expecting: '+f)
#                 self.assertTrue(f.strip() in all_findings, f)
