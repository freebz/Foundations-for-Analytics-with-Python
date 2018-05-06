supplies_view = columns_view(supplies, ['Supplier', 'Cost'])
print(supplies_view)
row_filter = supplies['Cost'] > 1000
supplies_row_column_filters = columns_view(supplies[row_filter], ['Supplier', 'Cost'])
print(supplies_total_cost_gt_1000_two_columns)
