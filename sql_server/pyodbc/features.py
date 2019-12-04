from django.db.backends.base.features import BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    """
    2019-08-30: Set all new Django 2.2 features to False, to see if I can
    upgrade. They may be worked upon later.

    https://docs.djangoproject.com/en/2.2/releases/2.2/

    2019-12-04: Same for Django 3 features.

    https://docs.djangoproject.com/en/3.0/releases/3.0/#backwards-incompatible-changes-in-3-0
    """
    allow_sliced_subqueries_with_in = False
    can_create_inline_fk = False
    can_introspect_autofield = True
    can_introspect_duration_field = False
    can_introspect_small_integer_field = True
    can_return_columns_from_insert = True
    can_use_chunked_reads = False
    for_update_after_from = True
    greatest_least_ignores_nulls = True
    has_real_datatype = True
    has_select_for_update = True
    has_select_for_update_nowait = True
    has_select_for_update_skip_locked = True
    has_zoneinfo_database = False
    ignores_table_name_case = True
    ignores_quoted_identifier_case = True
    requires_literal_defaults = True
    requires_sqlparse_for_splitting = False
    supports_ignore_conflicts = False
    supports_index_on_text_field = False
    supports_nullable_unique_constraints = True
    supports_paramstyle_pyformat = False
    supports_partial_indexes = False
    supports_partially_nullable_unique_constraints = False
    supports_regex_backreferencing = False
    supports_sequence_reset = False
    supports_subqueries_in_group_by = False
    supports_table_check_constraints = False
    supports_tablespaces = True
    supports_temporal_subtraction = True
    supports_timezones = False
    supports_transactions = True
    uses_savepoints = True
